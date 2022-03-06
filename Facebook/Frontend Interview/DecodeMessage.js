// Time = 0(N);
// Space = 0(1);

function decode(message) {
  let i = 0,
    j = 0,
    cols = message[0]?.length;
  let decoded = "",
    step = 1;

  while (j < cols) {
    decoded += message[i][j];
    if (!message[i + step]) {
      // check if I cannot move again
      step *= -1; // switch direction
    }
    i += step;
    j++;
  }

  return decoded;
}
