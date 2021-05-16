// Copyright: 兆边（上海）科技有限公司
// Author: 陈子轩
// Date: 2020-11-27
// Version: 1.1

#pragma once

// C++系统文件
#include <chrono>
#include <ctime>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

// 其他库.h文件
#include "PositionOffsetLLV_generated.h"
#include "flatbuffers/flatbuffers.h"

extern "C" {
#include "RoadsideUnit/asnDIGen/MessageFrame.h" /* MessageFrame ASN.1 type */
}
// 本地.h文件
#include "includes/mec_lib.h"
#include "includes/saveLog.h"

#define BUFFER_SIZE 2000
#define SIZE_OF_DESCRIPTION 4
#define LOG_HEAD_V2X "V2X_Flatbuffer :"


// Define Example V2X data frame to generate example data automatically
enum ExampleV2XFrame {
    ExampleV2XFrame_NOTHING,  /* No components present */
    ExampleV2XFrame_bsmFrame, // car
    ExampleV2XFrame_mapFrame,
    ExampleV2XFrame_rsmFrame,  // pedestrian
    ExampleV2XFrame_spatFrame, // signal
    ExampleV2XFrame_rsiFrame,  // events
};

class ExampleBSM {
private:
    // eps e-7
    uint32_t lon_;
    uint32_t lat_;

    // eps 0.02m/s
    uint16_t speed_;

    // eps 0.0125。
    uint32_t steering_;

public:
    /// <summary>
    ///
    /// </summary>
    /// <param name="data"></param>
    /// <returns>1 success 0 failed</returns>
    int SetDataFromV2X(const BasicSafetyMessage_t data);

    // local data management
    void Setlon(uint32_t lon) {
        if (lon >= 0 && lon <= 1800000001)
            this->lon_ = lon;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Longitude");
    }
    void Setlat(uint32_t lat) {
        if (lat >= 0 && lat <= 900000001)
            this->lat_ = lat;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Latitude");
    }
    void Setspeed(uint16_t speed) {
        if (speed >= 0 && speed <= 8191)
            this->speed_ = speed;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Speed");
    }
    void Setsteering(uint32_t steering) {
        if (steering >= 0 && steering <= 127)
            this->steering_ = steering;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Steering Angle");
    }

    uint32_t Getlon() const { return this->lon_; }
    uint32_t Getlat() const { return this->lat_; }
    uint16_t Getspeed() const { return this->speed_; }
    uint32_t Getsteering() const { return this->steering_; }
};

class ExampleMAP {};

class ExampleRSM {
private:
    // eps e-7
    uint32_t lon_;
    uint32_t lat_;

    // eps 0.02m/s
    uint16_t speed_;

    // eps 0.0125。
    uint32_t heading_;

public:
    /// <summary>
    ///
    /// </summary>
    /// <param name="data"></param>
    /// <returns>1 success 0 failed</returns>
    int SetDataFromV2X(const RoadsideSafetyMessage_t data);

    // local data management
    void Setlon(uint32_t lon) {
        if (lon >= 0 && lon <= 1800000001)
            this->lon_ = lon;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Longitude");
    }
    void Setlat(uint32_t lat) {
        if (lat >= 0 && lat <= 900000001)
            this->lat_ = lat;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Latitude");
    }
    void Setspeed(uint16_t speed) {
        if (speed >= 0 && speed <= 8191)
            this->speed_ = speed;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Speed");
    }
    void Setheading(uint32_t heading) {
        if (heading >= 0 && heading <= 28800)
            this->heading_ = heading;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Heading Angle");
    }

    uint32_t Getlon() const { return this->lon_; }
    uint32_t Getlat() const { return this->lat_; }
    uint16_t Getspeed() const { return this->speed_; }
    uint32_t Getheading() const { return this->heading_; }
};

class ExampleSPAT {
private:
    // id 0~255
    uint8_t phaseId_;

    // light 0~8
    uint8_t light_;

    // eps 0.1s =likelyendtime 0~35999
    uint16_t likelyEndTime_;

public:
    /// <summary>
    ///
    /// </summary>
    /// <param name="data"></param>
    /// <returns>1 success 0 failed</returns>
    int SetDataFromV2X(const SPAT_t data);

    // local data management
    void SetphaseId(uint8_t phaseId) {
        if (phaseId >= 0 && phaseId <= 255)
            this->phaseId_ = phaseId;
        else {
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__, "Wrong Value of the phaseId State");
        }
    }
    void Setlight(uint8_t light) {
        if (light >= 0 && light <= 8)
            this->light_ = light;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__, "Wrong Value of the Light State");
    }
    void SetlikelyEndTime(uint16_t likelyEndTime) {
        this->likelyEndTime_ = likelyEndTime % 36000;
    }
    uint8_t GetphaseId() const { return this->phaseId_; }
    uint8_t Getlight() const { return this->light_; }
    uint16_t GetlikelyEndTime() const { return this->likelyEndTime_; }
};

class ExampleRSI {
private:
    // eps e-7
    uint32_t lon_;
    uint32_t lat_;
    // two catagory of the events event[0] is larger than event[1]
    uint16_t event_;

    // eps 0.1m
    uint16_t radius_;

public:
    // 4 bytes maybe need to check
    char description[SIZE_OF_DESCRIPTION];

public:
    /// <summary>
    ///
    /// </summary>
    /// <param name="data"></param>
    /// <returns>1 success 0 failed</returns>
    int SetDataFromV2X(const RoadSideInformation_t data);

    // local data management
    void Setlon(uint32_t lon) {
        if (lon >= 0 && lon <= 1800000001)
            this->lon_ = lon;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Longitude");
    }
    void Setlat(uint32_t lat) {
        if (lat >= 0 && lat <= 900000001)
            this->lat_ = lat;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Latitude");
    }
    void Setevent(uint16_t event) { this->event_ = event; }
    void Setradius(uint16_t radius) {
        if (radius >= 0 && radius <= 1024)
            this->radius_ = radius;
        else
            CSaveLog::getInstance()->Info("%s %s : %s", LOG_HEAD_V2X,
                __FUNCTION__,
                "Wrong Value of the Radius");
    }
    uint32_t Getlon() const { return this->lon_; }
    uint32_t Getlat() const { return this->lat_; }
    uint16_t Getevent() const { return this->event_; }
    uint16_t Getradius() const { return this->radius_; }
};

class ExampleV2XData {
private:
    // Message Count from Upper Machine
    int MsgCnt_;

public:
    // Message type
    ExampleV2XFrame present;
    // Message Data
    union MessageFrame_u {
        ExampleBSM bsmFrame;
        ExampleMAP mapFrame;
        ExampleRSM rsmFrame;
        ExampleSPAT spatFrame;
        ExampleRSI rsiFrame;
    } choice;

public:
    ExampleV2XData() { present = ExampleV2XFrame_NOTHING; }

    ~ExampleV2XData() { present = ExampleV2XFrame_NOTHING; }

    /// <summary>
    /// convert the V2X into example data
    /// </summary>
    /// <param name="MF"></param>
    /// <param name="data"></param>
    /// <returns>1 success 0 failed</returns>
    int SetDataFromV2X(const MessageFrame_t data);

    /// <summary>
    /// convert the information into bytes
    /// </summary>
    /// <param name="Buffers"></param>
    /// <returns>length of encode message success 0 failed</returns>
    int GetBytesFromData(char* Buffers);

    // local data management
    void SetMsgCnt(int MsgCnt) { this->MsgCnt_ = MsgCnt % 128; }
    int GetMsgCnt() const { return this->MsgCnt_; }
};

/// <summary>
///
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int BSM2Fb(const MessageFrame_t* MF, std::shared_ptr<uint8_t[]>* data,
    size_t* size, long* type);

/// <summary>
///
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int SPAT2Fb(const MessageFrame_t* MF, std::shared_ptr<uint8_t[]>* data,
    size_t* size, long* type);

/// <summary>
///
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int RSI2Fb(const MessageFrame_t* MF, std::shared_ptr<uint8_t[]>* data,
    size_t* size, long* type);

/// <summary>
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int RSM2Fb(const MessageFrame_t* MF, std::shared_ptr<uint8_t[]>* data,
    size_t* size, long* type);

/// <summary>
///
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int MAP2Fb(const MessageFrame_t* MF, std::shared_ptr<uint8_t[]>* data,
    size_t* size, long* type);

/// <summary>
/// TS to RSI
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int TS2V2X(MessageFrame_t* MF, const void* data, const size_t* size,
    const long* type);

/// <summary>
/// TE to RSI
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int TE2V2X(MessageFrame_t* MF, const void* data, const size_t* size,
    const long* type);

/// <summary>
/// traffic signal SPAT to SPAT
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int SPAT2V2X(MessageFrame_t* MF, const void* data, const size_t* size,
    const long* type);

/// <summary>
/// MAP to MAP
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int MAP2V2X(MessageFrame_t* MF, const void* data, const size_t* size,
    const long* type);

/// <summary>
/// RSC to ?
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int RSC2V2X(MessageFrame_t* MF, const void* data, const size_t* size,
    const long* type);

/// <summary>
/// RSI to RSI ?
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int RSI2V2X(MessageFrame_t* MF, const void* data, const size_t* size,
    const long* type);

/// <summary>
/// RSM to RSM
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int RSM2V2X(MessageFrame_t* MF, const void* data, const size_t* size,
    const long* type);

/// <summary>
/// ?
/// </summary>
/// <param name="MF"></param>
/// <param name="data"></param>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns></returns>
int VIR2V2X(MessageFrame_t* MF, const void* data, const size_t* size,
    const long* type);

/// <summary>
/// get example flatbuffer data based on the type
/// </summary>
/// <param name="size"></param>
/// <param name="type"></param>
/// <returns>data ptr or nullptr</returns>
int ExampleFb(void*& data, size_t* size, const long type);

/// <summary>
/// get example message frame based on asn1c V2X msgframe
/// input:
///		MF:	        the pointer of asn1c message frame data
///		type:		data type
///     check:      if need to check
///  output:
///		int value: 1 if succeed, 0 otherwise
/// </summary>
int ExampleV2X(MessageFrame_t* MF, const long type, const ExampleV2XData* data,
    bool check = false);

/// <summary>
/// copy the PositionOffsetLLV message from flatbuffers to asn1c message
/// </summary>
/// <param name="pos"></param>
/// <param name="posoffLLV"></param>
/// <returns></returns>
PositionOffsetLLV_t
getPostionOffsetLLVfromFB(const MECData::DF_PositionOffsetLLV* posoffLLV);

/// <summary>
/// logBinary data in the filename
/// </summary>
int LogBinary(char* filename, char* data);

/// <summary>
/// 4 bytes to int
/// </summary>
/// <param name="num"></param>
/// <param name="bytes"></param>
int32_t Bytes2Int4(char* bytes);

/// <summary>
///  int4 to 4 bytes
/// need to delete[] the char*
/// </summary>
/// <param name="num"></param>
/// <param name="bytes"></param>
char* newInt42Bytes(int integer);

/// <summary>
/// int to char*
/// </summary>
/// <param name="i"></param>
/// <returns></returns>
char* newInt2Char(int i);

/// <summary>
/// double to char*
/// </summary>
/// <param name="i"></param>
/// <returns></returns>
char* newDouble2Char(double i);

/// <summary>
/// Transform bitstring to int8_t
/// </summary>
int8_t Bitstring2Int8_t(BIT_STRING_t bitstrint);

/// <summary>
/// generate the BIT_STRING
/// </summary>
/// <param name="bString"></param>
/// <param name="num"></param>
/// <param name="bufferSize"></param>
/// <param name="unusedBits"></param>
/// <returns>1 success 0 failed</returns>
int Int8_t2Bitstring(BIT_STRING_t* bString, int num, int bufferSize, int unusedBits);

/// <summary>
///  get the check buffer from the start to end index of the data, without
///  end.
/// </summary>
/// <param name="data"></param>
/// <param name="from"></param>
/// <param name="end"></param>
/// <returns>-1 if failed </returns>
int CheckByte(char* data, int start, int end);