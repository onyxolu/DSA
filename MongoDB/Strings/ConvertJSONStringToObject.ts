function jsonParse(jsonString: string): any {
  let currentPosition = 0;

  // Clarify: input always valid JSON? need to handle whitespace between tokens?
  //          escaped characters in strings (\" \\ \n)?
  //
  // Key insight: recursive descent parser — shared mutable position across all helpers
  // parseValue acts as dispatcher, routes to specific parser based on current character
  //
  // Volunteer before being asked:
  //   - Whitespace can appear between any tokens → skip it at start of parseValue and
  //     after consuming structural characters ({, }, [, ], :, ,)
  //   - Escaped characters in strings (\", \\, \n) need special handling, not just raw copy
  //   - Real world: this is literally how JSON.parse, XML parsers, and compilers work —
  //     same recursive descent pattern

  return parseValue();

  function skipWhitespace(): void {
    while (
      currentPosition < jsonString.length &&
      /\s/.test(jsonString[currentPosition])
    ) {
      currentPosition++;
    }
  }

  function parseValue(): any {
    skipWhitespace(); // handle leading whitespace before any value

    switch (jsonString[currentPosition]) {
      case '"':
        return parseString();
      case "{":
        return parseObject();
      case "[":
        return parseArray();
      case "t":
      case "f":
      case "n":
        return parseLiteral();
      default:
        return parseNumber();
    }
  }

  function parseNumber(): number {
    const startPosition = currentPosition;

    if (jsonString[currentPosition] === "-") {
      currentPosition++;
    }

    while (
      currentPosition < jsonString.length &&
      isDigit(jsonString[currentPosition])
    ) {
      currentPosition++;
    }

    if (jsonString[currentPosition] === ".") {
      currentPosition++;
      while (
        currentPosition < jsonString.length &&
        isDigit(jsonString[currentPosition])
      ) {
        currentPosition++;
      }
    }

    return Number(jsonString.slice(startPosition, currentPosition));
  }

  function parseString(): string {
    let parsedString = "";
    currentPosition++; // skip opening quote

    while (
      currentPosition < jsonString.length &&
      jsonString[currentPosition] !== '"'
    ) {
      if (jsonString[currentPosition] === "\\") {
        // handle escaped characters
        currentPosition++;
        const escapeChar = jsonString[currentPosition];
        const escapeMap: Record<string, string> = {
          '"': '"',
          "\\": "\\",
          n: "\n",
          t: "\t",
          r: "\r",
        };
        parsedString += escapeMap[escapeChar] ?? escapeChar;
      } else {
        parsedString += jsonString[currentPosition];
      }
      currentPosition++;
    }

    currentPosition++; // skip closing quote
    return parsedString;
  }

  function parseObject(): object {
    currentPosition++; // skip opening {
    const parsedObject: Record<string, any> = {};
    skipWhitespace();

    while (
      currentPosition < jsonString.length &&
      jsonString[currentPosition] !== "}"
    ) {
      skipWhitespace();
      const propertyName = parseString();
      skipWhitespace();
      expectCharacter(":");
      const propertyValue = parseValue();
      parsedObject[propertyName] = propertyValue;

      skipWhitespace();
      if (jsonString[currentPosition] === ",") {
        currentPosition++;
        skipWhitespace();
      }
    }

    currentPosition++; // skip closing }
    return parsedObject;
  }

  function parseArray(): any[] {
    currentPosition++; // skip opening [
    const parsedArray: any[] = [];
    skipWhitespace();

    while (
      currentPosition < jsonString.length &&
      jsonString[currentPosition] !== "]"
    ) {
      const arrayElement = parseValue();
      parsedArray.push(arrayElement);

      skipWhitespace();
      if (jsonString[currentPosition] === ",") {
        currentPosition++;
        skipWhitespace();
      }
    }

    currentPosition++; // skip closing ]
    return parsedArray;
  }

  function parseLiteral(): boolean | null {
    if (jsonString.startsWith("true", currentPosition)) {
      currentPosition += 4;
      return true;
    }
    if (jsonString.startsWith("false", currentPosition)) {
      currentPosition += 5;
      return false;
    }
    if (jsonString.startsWith("null", currentPosition)) {
      currentPosition += 4;
      return null;
    }
    throw new Error(`Unexpected token at position ${currentPosition}`);
  }

  function expectCharacter(expectedCharacter: string): void {
    skipWhitespace();
    if (jsonString[currentPosition] !== expectedCharacter) {
      throw new Error(
        `Expected '${expectedCharacter}' at position ${currentPosition}`,
      );
    }
    currentPosition++;
  }

  function isDigit(character: string): boolean {
    return character >= "0" && character <= "9";
  }
}

// Edge cases:
//   nested objects/arrays → handled via recursion through parseValue
//   whitespace between tokens → skipWhitespace called at key points
//   escaped characters in strings → escapeMap handles \" \\ \n \t \r
//   negative/decimal numbers → handled in parseNumber

// Complexity:
//   time  → O(n) — single pass through the string, each character visited once
//   space → O(d) recursion stack, d = max nesting depth

// Follow-ups:
//   Scientific notation numbers (1e10) → extend parseNumber to handle 'e'/'E'
//   Unicode escapes (\uXXXX) → extend escape handling in parseString
//   Streaming parser (don't have full string upfront) → much harder, need incremental state machine
//   Why not use a regex or JSON.parse directly? → this tests understanding of parsing fundamentals,
//                                                   same pattern used in real compilers/interpreters
