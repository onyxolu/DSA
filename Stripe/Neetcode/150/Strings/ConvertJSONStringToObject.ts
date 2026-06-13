function jsonParse(str: string): any {
   let i = 0;

   return parseValue();

   function parseValue(): any {
      switch (str[i]) {
         case '"':
            return parseString();
         case '{':
            return parseObject();
         case '[':
            return parseArray();
         case 't':
         case 'f':
         case 'n':
            return parseLiteral();
         default:
            return parseNumber();
      }
   }

   function parseNumber(): number {
      let start = i;

      if (str[i] === '-') {
         i++;
      }

      while (i < str.length && isDigit(str[i])) {
         i++;
      }

      if (str[i] === '.') {
         i++;
         while (i < str.length && isDigit(str[i])) {
            i++;
         }
      }

      return Number(str.slice(start, i));
   }

   function isDigit(n: string): boolean {
      return n >= '0' && n <= '9';
   }

   function parseString(): string {
      let result = '';
      i++;

      while (i < str.length && str[i] !== '"') {
         result += str[i];
         i++;
      }

      i++;
      return result;
   }

   function parseObject(): Object {
      i++;

      const result: any = {};

      while (i < str.length && str[i] !== '}') {
         const key = parseString();
         expectChar(':');
         const value = parseValue();

         result[key] = value;
         if (str[i] === ',') {
            i++;
         }
      }

      i++;
      return result;
   }

   function parseArray(): any[] {
      i++;

      const result: any[] = [];

      while (i < str.length && str[i] !== ']') {
         const value = parseValue();
         result.push(value);
         if (str[i] === ',') {
            i++;
         }
      }

      i++;
      return result;
   }

   function parseLiteral(): boolean | null {
      if (str.startsWith('true', i)) {
         i += 4;
         return true;
      } else if (str.startsWith('false', i)) {
         i += 5;
         return false;
      } else if (str.startsWith('null', i)) {
         i += 4;
         return null;
      }
      throw new Error(`Unexpected token at position ${i}`);
   }

   function expectChar(char: string): void {
      if (str[i] !== char) {
         throw new Error(`Expected '${char}' at position ${i}`);
      }
      i++;
   }
}