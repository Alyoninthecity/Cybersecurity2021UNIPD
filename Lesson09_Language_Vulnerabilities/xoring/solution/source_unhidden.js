var baka = [
    "",
    "\x66\x72\x6F\x6D\x43\x68\x61\x72\x43\x6F\x64\x65", //fromCharCode
    "\x6C\x65\x6E\x67\x74\x68", //length
    "\x73\x75\x62\x73\x74\x72", //substr
];
function x(pass, stringSix) {
    var a = [];
    var result = "";
    for (z = 1; z <= 255; z++) {
        a[String.fromCharCode(z)] = z; 
    }
    for (j = z = 0; z < pass.length; z++) {
        result += String.fromCharCode(
            a[pass.substr(z, 1)] ^ a[stringSix.substr(j, 1)]
        );
        j = j < stringSix.length ? j + 1 : 0;
    }
    return result;
}

console.log(x("_NeAM+bh_saaES_mFlSYYu}nYw}", "6"));
