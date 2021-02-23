# Libcurl based 

https://blog.csdn.net/lvyibin890/article/details/81040971?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=7c06173d-1168-40a6-bee8-eddceb42e05d&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control
libcurl的基本编程流程
1. 调用curl_global_init()初始化libcurl
2. 调用 curl_easy_init()函数得到 easy interface型指针
3. 调用curl_easy_setopt设置传输选项
4. 根据curl_easy_setopt设置的传输选项，实现回调函数以完成用户特定任务
5. 调用curl_easy_perform（）函数完成传输任务
6. 调用curl_easy_cleanup（）释放内存

# C++ wrapper based on Libcurl
1. curlpp
2. curlcpp
3. https://github.com/mr5z/cppurl

# Boost Beast


# CROW
https://github.com/ipkn/crow
