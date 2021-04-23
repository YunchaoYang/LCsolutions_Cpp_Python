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
<p><span style="color:#86ca5e;"><strong>3. ^$ 表示字符串的结尾，匹配输入字符串结尾的位置；</strong></span></p> 
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
