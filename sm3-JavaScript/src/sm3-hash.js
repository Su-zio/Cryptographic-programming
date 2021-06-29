/*
 * @Author: kok-s0s
 * @Date: 2021-06-30 00:44:44
 * @LastEditors: kok-s0s
 * @LastEditTime: 2021-06-30 01:14:05
 * @Description: file content
 */

const sm3 = require('sm-crypto').sm3;

let hashData = sm3();

console.log(hashData);