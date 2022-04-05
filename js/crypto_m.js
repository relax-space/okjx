const e =require('crypto-js')
// 加密shouquan.php参数,用这个key: dvyYRQlnPRCMdQSe 
// 解密m3u8用这个key: 36606EE9A59DDCE2 

const decrypt = function (text,key, iv) {
  return e.AES.decrypt(text, 
  e.enc.Latin1.parse(key), {
   iv:e.enc.Latin1.parse(iv),
   mode: e.mode.CBC,
   padding: e.pad.NoPadding,
  }).toString(e.enc.Utf8)
 }

const encrypt = function (text,key, iv) {

    return e.AES.encrypt(text, e.enc.Latin1.parse(key), {
      iv:e.enc.Latin1.parse(iv),
      mode: e.mode.CBC,
      padding: e.pad.Pkcs7
    }).toString()
  }


// "m3u8.okjx.cc|c98851835f93fa6f"
// console.log(encrypt('m3u8.okjx.cc|c98851835f93fa6f'
// ,"dvyYRQlnPRCMdQSe"
// ,"c98851835f93fa6f"))

// console.log(decrypt("30c25uTdfskwm_SSJiQilcQQJJx8xJuICSO50JTbn2_C2CkNJAQhKBquhxyJ2rLAXzcefukHFzT9SXVvoTyTRRQGx4pONlIc_jCIhkBtzr9uFnp5jfQw6b_UHdr-9FE7yCexRm56cS71mJ9UTQ"
// ,"36606EE9A59DDCE2"
// ,"9736816ac990d84f"))




