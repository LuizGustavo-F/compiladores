; ModuleID = "arara_program"
source_filename = "arara.arara"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str.0 = private unnamed_addr constant [25 x i8] c"\44\69\67\69\74\65\20\75\6D\20\76\61\6C\6F\72\20\70\61\72\61\20\61\3A\0A\00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"\25\64\0A\00", align 1
@.str.2 = private unnamed_addr constant [3 x i8] c"\25\64\00", align 1
@.str.3 = private unnamed_addr constant [25 x i8] c"\44\69\67\69\74\65\20\75\6D\20\76\61\6C\6F\72\20\70\61\72\61\20\62\3A\0A\00", align 1

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:
    %a_ptr = alloca i32, align 4
    %b_ptr = alloca i32, align 4
    %valor_ptr = alloca i32, align 4
    %temp0 = getelementptr inbounds i8, [25 x i8]* @.str.0, i64 0, i64 0
    %call_printf_%temp1 = call i32 (i8*, ...) @printf(i8* %temp0)
    %temp2 = getelementptr inbounds i8, [3 x i8]* @.str.2, i64 0, i64 0
    %call_scanf_%temp3 = call i32 (i8*, ...) @scanf(i8* %temp2, i32* %a_ptr)
    %temp4 = getelementptr inbounds i8, [25 x i8]* @.str.3, i64 0, i64 0
    %call_printf_%temp5 = call i32 (i8*, ...) @printf(i8* %temp4)
    %temp6 = getelementptr inbounds i8, [3 x i8]* @.str.2, i64 0, i64 0
    %call_scanf_%temp7 = call i32 (i8*, ...) @scanf(i8* %temp6, i32* %b_ptr)
    %temp8 = load i32, i32* %a_ptr, align 4
    %temp9 = load i32, i32* %b_ptr, align 4
    %_t0 = add i32 %temp8, %temp9
    store i32 %_t0, i32* %valor_ptr, align 4
    %temp10 = load i32, i32* %valor_ptr, align 4
    %temp11 = getelementptr inbounds i8, [4 x i8]* @.str.1, i64 0, i64 0
    %call_printf_%temp12 = call i32 (i8*, ...) @printf(i8* %temp11, i32 %temp10)
    ret i32 0
}