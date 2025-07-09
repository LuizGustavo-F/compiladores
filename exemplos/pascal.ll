; ModuleID = "arara_program"
source_filename = "arara.arara"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str.0 = private unnamed_addr constant [3 x i8] c"\25\64\00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"\25\64\20\00", align 1
@.str.2 = private unnamed_addr constant [43 x i8] c"\49\6E\73\69\72\61\20\75\6D\20\76\61\6C\6F\72\20\70\61\72\61\20\6F\20\74\72\69\61\6E\67\75\6C\6F\20\64\65\20\70\61\73\63\61\6C\00", align 1
@.str.3 = private unnamed_addr constant [2 x i8] c"\20\00", align 1
@.str.4 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:
    %C_ptr = alloca i32, align 4
    %i_ptr = alloca i32, align 4
    %j_ptr = alloca i32, align 4
    %linha_ptr = alloca i32, align 4
    %n_ptr = alloca i32, align 4
    br label %start_code
start_code:
    %t0 = getelementptr inbounds [43 x i8], [43 x i8]* @.str.2, i64 0, i64 0
    %t1 = call i32 (i8*, ...) @printf(i8* %t0)
    %t2 = getelementptr inbounds [3 x i8], [3 x i8]* @.str.0, i64 0, i64 0
    %t3 = call i32 (i8*, ...) @scanf(i8* %t2, i32* %n_ptr)
    store i32 0, i32* %linha_ptr, align 4
    br label %L0
L0:
    %t4 = load i32, i32* %linha_ptr, align 4
    %t5 = load i32, i32* %n_ptr, align 4
    %_t0 = icmp slt i32 %t4, %t5
    br i1 %_t0, label %b0, label %L1
b0:
    store i32 0, i32* %j_ptr, align 4
    br label %L2
L2:
    %t6 = load i32, i32* %n_ptr, align 4
    %t7 = load i32, i32* %linha_ptr, align 4
    %_t1 = sub i32 %t6, %t7
    %_t2 = sub i32 %_t1, 1
    %t8 = load i32, i32* %j_ptr, align 4
    %_t3 = icmp slt i32 %t8, %_t2
    br i1 %_t3, label %b1, label %L3
b1:
    %t9 = getelementptr inbounds [2 x i8], [2 x i8]* @.str.3, i64 0, i64 0
    %t10 = call i32 (i8*, ...) @printf(i8* %t9)
    %t11 = load i32, i32* %j_ptr, align 4
    %_t4 = add i32 %t11, 1
    store i32 %_t4, i32* %j_ptr, align 4
    br label %L2
L3:
    store i32 1, i32* %C_ptr, align 4
    store i32 0, i32* %i_ptr, align 4
    br label %L4
L4:
    %t12 = load i32, i32* %i_ptr, align 4
    %t13 = load i32, i32* %linha_ptr, align 4
    %_t5 = icmp sle i32 %t12, %t13
    br i1 %_t5, label %b2, label %L5
b2:
    %t14 = load i32, i32* %C_ptr, align 4
    %t15 = getelementptr inbounds [4 x i8], [4 x i8]* @.str.1, i64 0, i64 0
    %t16 = call i32 (i8*, ...) @printf(i8* %t15, i32 %t14)
    %t17 = load i32, i32* %linha_ptr, align 4
    %t18 = load i32, i32* %i_ptr, align 4
    %_t6 = sub i32 %t17, %t18
    %t19 = load i32, i32* %C_ptr, align 4
    %_t7 = mul i32 %t19, %_t6
    %t20 = load i32, i32* %i_ptr, align 4
    %_t8 = add i32 %t20, 1
    %_t9 = sdiv i32 %_t7, %_t8
    store i32 %_t9, i32* %C_ptr, align 4
    %t21 = load i32, i32* %i_ptr, align 4
    %_t10 = add i32 %t21, 1
    store i32 %_t10, i32* %i_ptr, align 4
    br label %L4
L5:
    %t22 = getelementptr inbounds [2 x i8], [2 x i8]* @.str.4, i64 0, i64 0
    %t23 = call i32 (i8*, ...) @printf(i8* %t22)
    %t24 = load i32, i32* %linha_ptr, align 4
    %_t11 = add i32 %t24, 1
    store i32 %_t11, i32* %linha_ptr, align 4
    br label %L0
L1:
    ret i32 0
}