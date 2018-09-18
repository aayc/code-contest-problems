/*
Written for the Google Advanced Programming course, first module.
Define a decompression method that will take 2[hey3[a]]c and turn it into heyaaaheyaaac

The input will always be syntactically correct.
*/

function isDigit(s) {
  return "0123456789".includes(s)
}

function decompress(s, startIx = 0, repeater = 1) {
  var ret = ""
  var d = ""

  for (let i = startIx; i < s.length; i++) {
    if (s[i] == "[") {
      let decomped = decompress(s, i + 1, parseInt(d))
      d = ""

      j = decomped.length - 1
      while (isDigit(decomped[j])) j--;
      
      let skipTo = parseInt(decomped.substr(j + 1))
      ret += decomped.substr(0, j + 1)
      i = skipTo
    }
    else if (s[i] == "]") {
      // returning i will actually mean the next character to be examined is i + 1
      return repStr(ret, repeater) + i
    }
    else if (isDigit(s[i])) {
      d += s[i]
    }
    else {
      ret += s[i]
    }
  }
  return ret
}

function repStr (s, n) {
  let ret = ""
  for (let i = 0; i < n; i++)
    ret += s
  return ret
}
console.log(decompress("a2[hey3[hi]a]d2[]cdwaf"));