<div id="article_content" class="article_content clearfix">
        <link rel="stylesheet" href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/editerView/ck_htmledit_views-b5506197d8.css">
                <div id="content_views" class="htmledit_views">
<h3><a name="t1"></a><a name="t1"></a><span style="color:#3399ea;"><strong>常用函数：</strong></span></h3> 
<p><strong><a href="http://www.cplusplus.com/reference/regex/regex_match/"><span style="color:#7c79e5;">regex_match</span></a><span style="color:#86ca5e;">：全文匹配，要求整个字符串符合正则表达式的匹配规则。</span></strong><strong><span style="color:#86ca5e;">用来判断一个字符串和一个正则表达式是否模式匹配，如果匹配成功则返回<code>true</code>，否则返回<code>false</code>。</span></strong></p> 
<p><strong><a href="http://www.cplusplus.com/reference/regex/regex_search/"><span style="color:#7c79e5;">regex_search</span></a><span style="color:#86ca5e;">：搜索匹配，根据正则表达式来搜索字符串中是否存在符合规则的子字符串。</span></strong></p> 
<p><strong><a href="http://www.cplusplus.com/reference/regex/regex_replace/"><span style="color:#7c79e5;">regex_</span></a><span style="color:#7c79e5;">replace</span><span style="color:#86ca5e;">：替换匹配，即可以将符合匹配规则的子字符串替换为其他字符串。</span></strong><strong><span style="color:#86ca5e;">要求输入一个正则表达式，以及一个用于替换匹配子字符串的格式化字符串。这个格式化字符串可以通过转义序列引用匹配子字符串中的部分内容。</span></strong></p> 
<h3><a name="t2"></a><a name="t2"></a><span style="color:#3399ea;"><strong>语法规则：</strong></span></h3> 
<p><span style="color:#86ca5e;"><strong>1. \ 表示将下一字符标记为特殊字符、转义字符；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>2. ^ 表示字符串的开始，匹配输入字符串开始的位置；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>3. $ 表示字符串的结尾，匹配输入字符串结尾的位置；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>4. .&nbsp;表示匹配除换行符" \n "以外的任意字符；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>5.&nbsp;\w 表示任意字母、数字、下划线 ；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>6. \s 表示任意空白符(tab也包含在内)；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>7. \d 表示匹配单个数字字符，\D 表示非数字字符匹配；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>8. [] 表示一个字符集合，</strong></span><strong><span style="color:#86ca5e;">匹配指定范围内的任何字符，</span></strong><span style="color:#86ca5e;"><strong>例如[a-z]表示字母a~z所组成的集合；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>9.&nbsp;[]中使用^来表示集合的补集，匹配不在指定的范围内的任何字符，例如[^1-3]表示除1 2 3以外数字；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>10. [[:alpha:]] 表示任何字母；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>11. [[:alnum:]] 表示任何字母和数字；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>12. regex::icase 表示匹配时忽略大小写；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>13.&nbsp;{<!-- --><em>n</em>} 表示正好匹配&nbsp;<em>n</em>&nbsp;次前面的字符或表达式，例如"hello{6}",匹配字符串中符合第二个l后边有6个o的子字符串；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>14. {n, } 表示至少匹配 n 次前面的字符或表达式；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>15. {n,m} 表示匹配至少&nbsp;<em>n</em>&nbsp;次，至多&nbsp;<em>m</em>&nbsp;次前面的字符或表达式；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>16. * 表示零次或多次匹配前面的字符或子表达式，等效于{0, }；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>17. + 表示一次或多次匹配前面的字符或子表达式；</strong></span></p> 
<p><span style="color:#86ca5e;"><strong>18.&nbsp;?&nbsp;表示零次或一次匹配前面的字符或子表达式；</strong></span></p> 
<p><strong><span style="color:#86ca5e;">19. \t \n&nbsp;\r这些平时非常常见，分别表示制表符匹配、换行符匹配、回车符匹配。</span></strong></p> 
</div>
        
        
```cpp
#include<regex>
```
- regex  双斜杠转义 

- 日期的格式是：2020-01-01
- \d{4}-\d{2}-\d{2}

有了正则表达式之后，你需要将你的文本和正则表达式交给正则表达式引擎 – 由C++语言（或者其他语言）提供。引擎会在文本中搜索到匹配的结果。请注意，正则表达式有它自身的语法。这与C++的语法是两回事。C++编译器只会检查C++代码的语法。

### 匹配 regex_match
匹配是判断给定的字符串是否符合某个正则表达式。例如：你想判断当前文本是否全部由数字构成。
```cpp
string s1 = "ab123cdef"; // ①
string s2 = "123456789"; // ②
regex ex("\\d+"); // ③
cout << s1 << " is all digit: " << regex_match(s1, ex) << endl; // ④ false
cout << s2 << " is all digit: " << regex_match(s2, ex) << endl; // ⑤ true
```
### 搜索 regex_search
还有一些时候，我们要判断的并非是文本的全体是否匹配。而是在一大段文本中搜索匹配的目标。

```cpp
string s = "ab123cdef"; // ①
regex ex("\\d+");    // ②

smatch match; // ③ std::smatch来保存匹配的结果。除了std::smatch
regex_search(s, match, ex); // ④
cout << s << " contains digit: " << match[0] << endl; // ⑤  123
```

### 替换 regex_replace
最后，使用正则表达式的还有一个常见功能是文本替换。很多的编辑器都有这样的功能。
```cpp
string s = "ab123cdef"; // ①
regex ex("\\d+");    // ②
string r = regex_replace(s, ex, "xxx"); // ③
cout << r << endl; // ④ abxxxcdef
```

### C++中内置了多种正则表达式文法，在创建正则表达式的时候可以通过参数来选择。
<table>
  <thead>
    <tr>
      <th>文法</th>
      <th>说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ECMAScript</td>
      <td><a href="https://en.cppreference.com/w/cpp/regex/ecmascript">ECMAScript正则表达式语法</a>，默认选项</td>
    </tr>
    <tr>
      <td>basic</td>
      <td><a href="http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_03">基础POSIX正则表达式语法</a></td>
    </tr>
    <tr>
      <td>extended</td>
      <td><a href="http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_04">扩展POSIX正则表达式语法</a></td>
    </tr>
    <tr>
      <td>awk</td>
      <td><a href="http://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_04">awk工具的正则表达式语法</a></td>
    </tr>
    <tr>
      <td>grep</td>
      <td><a href="https://www.gnu.org/software/findutils/manual/html_node/find_html/grep-regular-expression-syntax.html">grep工具的正则表达式语法</a></td>
    </tr>
    <tr>
      <td>egrep</td>
      <td><a href="https://www.gnu.org/software/findutils/manual/html_node/find_html/posix_002degrep-regular-expression-syntax.html#posix_002degrep-regular-expression-syntax">grep工具的正则表达式语法</a></td>
    </tr>
  </tbody>
</table>

### Raw string literal
在代码中写字符串有时候是比较麻烦的，因为很多字符需要通过反斜杠转义。当有多个反斜杠连在一起时，就很容易写错或者理解错了。

当通过字符串来写正则表达式时，这个问题就更严重了。因为正则表达式本身也有一些字符需要转义。例如，对于这样一个字符串 "('(?:[^\\\\']|\\\\.)*'|\"(?:[^\\\\\"]|\\\\.)*\")|" 大部分人恐怕很难一眼看出其含义了。

在正则表达式很复杂的时候，推荐大家使用Raw string literal来表达。这种表达式是告诉编译器：这里的内容是纯字符串，因此不再需要增加反斜杠来转义特殊字符。

Raw string literal的格式如下：
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight" style="position: relative;"><code>R"delimiter(raw_characters)delimiter"
</code><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre></div></div>
<p>这其中：</p>
<ul>
  <li>delimiter是可选的分隔符，通常不用写</li>
  <li>raw_characters是具体的字符串</li>
</ul>

<p>也就是说，
        <code class="language-plaintext highlighter-rouge">R"(content)"</code>中的
        <code class="language-plaintext highlighter-rouge">content</code>是你需要的字符串本身。
</p>


Reference
1. https://paul.pub/cpp-regex/
2. https://blog.csdn.net/Piconjo/article/details/104578265?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_utm_term-5&spm=1001.2101.3001.4242

### Examples
```cpp
String qq="1234567";
boolean b=qq.matches("[1-9][0-9]{4,10}");
// [1-9]代表第一位数必须在1和9之间 
// [0-9]{4,10} 代表范围 [0-9] 出现至少 4 次，但是不超过 11 次
```

```cpp
String ip="192.168.1.1";
boolean b=ip.matches("([0-9]{0,3}\\.){3}[0-9]{0,3}");
// ([0-9]{0,3}\\.){3} -- 代表 ([0-9]{0,3}\\.) 出现3次。
// 展开既是： 
// ([0-9]{0,3}\\.) ([0-9]{0,3}\\.) ([0-9]{0,3}\\.) [0-9]{0,3}
// -------------.|--------------.|---------------.|-----------|
//       192    .       168     .          1     .      1
```

```cpp
String ip = "192.168.1.1";
String[] aa = ip.split("\\.");
//若regex为.的话 必须加双斜杠转义 否则无效
```
```cpp
// 敏感词/违禁词屏蔽：
String dirtySay = "Hello暴血暴力暴血血腥暴血World";
String cleanSay = dirtySay.replaceAll("(暴力|血腥)+", "*");/*替换All全部违禁词*/
```
```cpp
String str = "   12          44    68  piconjo     19    36 ";//中间穿插着随机长度的空格
String[] a = str.trim().split(" +");
```
