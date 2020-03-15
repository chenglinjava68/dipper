package com.dipper.phecda.entity;

import lombok.Data;

@Data
public class MVUser {

    private Integer id;            //我的ID,即userId
    private String username;   //我的真是姓名，即ucName
    private String status;     //在线状态 online：在线、hide：隐身
    private String sign;       //我的签名
    private String avatar;     //我的头像

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }

    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }

    @Override
    public String toString() {
        return "MVUser{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", status='" + status + '\'' +
                ", sign='" + sign + '\'' +
                ", avatar='" + avatar + '\'' +
                '}';
    }
}
