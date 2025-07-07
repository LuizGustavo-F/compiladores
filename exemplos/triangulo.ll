; ModuleID = "arara_program"
source_filename = "arara.arara"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str.0 = private unnamed_addr constant [27 x i8] c"\45\6E\74\72\65\20\63\6F\6D\20\75\6D\20\76\61\6C\6F\72\20\70\61\72\61\20\41\0A\00", align 1
@.str.1 = private unnamed_addr constant [3 x i8] c"\25\64\00", align 1
@.str.2 = private unnamed_addr constant [27 x i8] c"\45\6E\74\72\65\20\63\6F\6D\20\75\6D\20\76\61\6C\6F\72\20\70\61\72\61\20\42\0A\00", align 1
@.str.3 = private unnamed_addr constant [27 x i8] c"\45\6E\74\72\65\20\63\6F\6D\20\75\6D\20\76\61\6C\6F\72\20\70\61\72\61\20\43\0A\00", align 1
@.str.4 = private unnamed_addr constant [29 x i8] c"\54\72\69\61\6E\67\75\6C\6F\20\65\71\75\69\6C\61\74\65\72\6F\20\76\61\6C\69\64\6F\0A\00", align 1
@.str.5 = private unnamed_addr constant [28 x i8] c"\54\72\69\61\6E\67\75\6C\6F\20\69\73\6F\73\63\65\6C\65\73\20\76\61\6C\69\64\6F\0A\00", align 1
@.str.6 = private unnamed_addr constant [27 x i8] c"\54\72\69\61\6E\67\75\6C\6F\20\65\73\63\61\6C\65\6E\6F\20\76\61\6C\69\64\6F\0A\00", align 1
@.str.7 = private unnamed_addr constant [19 x i8] c"\4D\65\64\69\64\61\73\20\69\6E\76\61\6C\69\64\61\73\0A\00", align 1
@.str.8 = private unnamed_addr constant [52 x i8] c"\45\72\72\6F\3A\20\76\61\6C\6F\72\65\73\20\6E\65\67\61\74\69\76\6F\73\20\6F\75\20\7A\65\72\6F\20\6E\61\6F\20\73\61\6F\20\70\65\72\6D\69\74\69\64\6F\73\0A\00", align 1

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:
    %a_ptr = alloca i32, align 4
    %b_ptr = alloca i32, align 4
    %c_ptr = alloca i32, align 4
    %temp0 = getelementptr inbounds [27 x i8], [27 x i8]* @.str.0, i64 0, i64 0
    %temp1 = call i32 (i8*, ...) @printf(i8* %temp0)
    %temp2 = getelementptr inbounds [3 x i8], [3 x i8]* @.str.1, i64 0, i64 0
    %temp3 = call i32 (i8*, ...) @scanf(i8* %temp2, i32* %a_ptr)
    %temp4 = getelementptr inbounds [27 x i8], [27 x i8]* @.str.2, i64 0, i64 0
    %temp5 = call i32 (i8*, ...) @printf(i8* %temp4)
    %temp6 = getelementptr inbounds [3 x i8], [3 x i8]* @.str.1, i64 0, i64 0
    %temp7 = call i32 (i8*, ...) @scanf(i8* %temp6, i32* %b_ptr)
    %temp8 = getelementptr inbounds [27 x i8], [27 x i8]* @.str.3, i64 0, i64 0
    %temp9 = call i32 (i8*, ...) @printf(i8* %temp8)
    %temp10 = getelementptr inbounds [3 x i8], [3 x i8]* @.str.1, i64 0, i64 0
    %temp11 = call i32 (i8*, ...) @scanf(i8* %temp10, i32* %c_ptr)
    %temp12 = load i32, i32* %a_ptr, align 4
    %temp13 = load i32, i32* %b_ptr, align 4
    %_t3 = add i32 %temp12, %temp13
    %temp14 = load i32, i32* %a_ptr, align 4
    %temp15 = load i32, i32* %c_ptr, align 4
    %_t5 = add i32 %temp14, %temp15
    %temp16 = getelementptr inbounds [29 x i8], [29 x i8]* @.str.4, i64 0, i64 0
    %temp17 = call i32 (i8*, ...) @printf(i8* %temp16)
    %temp18 = getelementptr inbounds [28 x i8], [28 x i8]* @.str.5, i64 0, i64 0
    %temp19 = call i32 (i8*, ...) @printf(i8* %temp18)
    %temp20 = getelementptr inbounds [27 x i8], [27 x i8]* @.str.6, i64 0, i64 0
    %temp21 = call i32 (i8*, ...) @printf(i8* %temp20)
    %temp22 = getelementptr inbounds [19 x i8], [19 x i8]* @.str.7, i64 0, i64 0
    %temp23 = call i32 (i8*, ...) @printf(i8* %temp22)
    %temp24 = getelementptr inbounds [52 x i8], [52 x i8]* @.str.8, i64 0, i64 0
    %temp25 = call i32 (i8*, ...) @printf(i8* %temp24)
    ret i32 0
}