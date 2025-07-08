; ModuleID = "arara_program"
source_filename = "arara.arara"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str.0 = private unnamed_addr constant [3 x i8] c"\25\64\00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"\25\64\20\00", align 1
@.str.2 = private unnamed_addr constant [22 x i8] c"\44\69\67\69\74\65\20\6F\20\76\61\6C\6F\72\20\64\65\20\41\3A\20\00", align 1
@.str.3 = private unnamed_addr constant [22 x i8] c"\44\69\67\69\74\65\20\6F\20\76\61\6C\6F\72\20\64\65\20\42\3A\20\00", align 1
@.str.4 = private unnamed_addr constant [22 x i8] c"\44\69\67\69\74\65\20\6F\20\76\61\6C\6F\72\20\64\65\20\43\3A\20\00", align 1
@.str.5 = private unnamed_addr constant [28 x i8] c"\54\72\69\61\6E\67\75\6C\6F\20\65\71\75\69\6C\61\74\65\72\6F\20\76\61\6C\69\64\6F\00", align 1
@.str.6 = private unnamed_addr constant [27 x i8] c"\54\72\69\61\6E\67\75\6C\6F\20\69\73\6F\73\63\65\6C\65\73\20\76\61\6C\69\64\6F\00", align 1
@.str.7 = private unnamed_addr constant [26 x i8] c"\54\72\69\61\6E\67\75\6C\6F\20\65\73\63\61\6C\65\6E\6F\20\76\61\6C\69\64\6F\00", align 1
@.str.8 = private unnamed_addr constant [18 x i8] c"\4D\65\64\69\64\61\73\20\69\6E\76\61\6C\69\64\61\73\00", align 1
@.str.9 = private unnamed_addr constant [51 x i8] c"\45\72\72\6F\3A\20\76\61\6C\6F\72\65\73\20\6E\65\67\61\74\69\76\6F\73\20\6F\75\20\7A\65\72\6F\20\6E\61\6F\20\73\61\6F\20\70\65\72\6D\69\74\69\64\6F\73\00", align 1

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:
    %a_ptr = alloca i32, align 4
    %b_ptr = alloca i32, align 4
    %c_ptr = alloca i32, align 4
    br label %start_code
start_code:
    %t0 = getelementptr inbounds [22 x i8], [22 x i8]* @.str.2, i64 0, i64 0
    %t1 = call i32 (i8*, ...) @printf(i8* %t0)
    %t2 = getelementptr inbounds [3 x i8], [3 x i8]* @.str.0, i64 0, i64 0
    %t3 = call i32 (i8*, ...) @scanf(i8* %t2, i32* %a_ptr)
    %t4 = getelementptr inbounds [22 x i8], [22 x i8]* @.str.3, i64 0, i64 0
    %t5 = call i32 (i8*, ...) @printf(i8* %t4)
    %t6 = getelementptr inbounds [3 x i8], [3 x i8]* @.str.0, i64 0, i64 0
    %t7 = call i32 (i8*, ...) @scanf(i8* %t6, i32* %b_ptr)
    %t8 = getelementptr inbounds [22 x i8], [22 x i8]* @.str.4, i64 0, i64 0
    %t9 = call i32 (i8*, ...) @printf(i8* %t8)
    %t10 = getelementptr inbounds [3 x i8], [3 x i8]* @.str.0, i64 0, i64 0
    %t11 = call i32 (i8*, ...) @scanf(i8* %t10, i32* %c_ptr)
    %t12 = load i32, i32* %a_ptr, align 4
    %_t0 = icmp sgt i32 %t12, 0
    %t13 = load i32, i32* %b_ptr, align 4
    %_t1 = icmp sgt i32 %t13, 0
    %_t2 = and i1 %_t0, %_t1
    br i1 %_t2, label %b0, label %L0
b0:
    %t14 = load i32, i32* %a_ptr, align 4
    %t15 = load i32, i32* %b_ptr, align 4
    %_t3 = add i32 %t14, %t15
    %t16 = load i32, i32* %c_ptr, align 4
    %_t4 = icmp sgt i32 %_t3, %t16
    %t17 = load i32, i32* %a_ptr, align 4
    %t18 = load i32, i32* %c_ptr, align 4
    %_t5 = add i32 %t17, %t18
    %t19 = load i32, i32* %b_ptr, align 4
    %_t6 = icmp sgt i32 %_t5, %t19
    %_t7 = and i1 %_t4, %_t6
    br i1 %_t7, label %b1, label %L2
b1:
    %t20 = load i32, i32* %a_ptr, align 4
    %t21 = load i32, i32* %b_ptr, align 4
    %_t8 = icmp eq i32 %t20, %t21
    %t22 = load i32, i32* %b_ptr, align 4
    %t23 = load i32, i32* %c_ptr, align 4
    %_t9 = icmp eq i32 %t22, %t23
    %_t10 = and i1 %_t8, %_t9
    br i1 %_t10, label %b2, label %L4
b2:
    %t24 = getelementptr inbounds [28 x i8], [28 x i8]* @.str.5, i64 0, i64 0
    %t25 = call i32 (i8*, ...) @printf(i8* %t24)
    br label %L5
L4:
    %t26 = load i32, i32* %a_ptr, align 4
    %t27 = load i32, i32* %b_ptr, align 4
    %_t11 = icmp eq i32 %t26, %t27
    %t28 = load i32, i32* %a_ptr, align 4
    %t29 = load i32, i32* %c_ptr, align 4
    %_t12 = icmp eq i32 %t28, %t29
    %_t13 = or i1 %_t11, %_t12
    br i1 %_t13, label %b3, label %L6
b3:
    %t30 = getelementptr inbounds [27 x i8], [27 x i8]* @.str.6, i64 0, i64 0
    %t31 = call i32 (i8*, ...) @printf(i8* %t30)
    br label %L7
L6:
    %t32 = getelementptr inbounds [26 x i8], [26 x i8]* @.str.7, i64 0, i64 0
    %t33 = call i32 (i8*, ...) @printf(i8* %t32)
    br label %L7
L7:
    br label %L5
L5:
    br label %L3
L2:
    %t34 = getelementptr inbounds [18 x i8], [18 x i8]* @.str.8, i64 0, i64 0
    %t35 = call i32 (i8*, ...) @printf(i8* %t34)
    br label %L3
L3:
    br label %L1
L0:
    %t36 = getelementptr inbounds [51 x i8], [51 x i8]* @.str.9, i64 0, i64 0
    %t37 = call i32 (i8*, ...) @printf(i8* %t36)
    br label %L1
L1:
    ret i32 0
}