## �p�r

�e�ʂ̑傫���t�H���_��t�@�C����100MB�ɕ������A�D����png�ɖ��ߍ���

zip-as-png-py���ہX���p
https://github.com/yoshi389111/zip-as-png-py

file2png.py�F�t�@�C����zip����png�ɖ��ߍ���
png2file.py�F��������png�����ɖ߂�

## �Z�b�g�A�b�v

���t�@�C��
file2png.py�F14�`17�s�ځ@�p�X��K�X�ύX
png2file.py�F9�s�ځ@�p�X��K�X�ύX

���p�X
base�Fzip�𖄂ߍ��ޑΏۉ摜������ꏊ
inputs�F����zip�A��zip�����ꎞ�I�ɒu���ꏊ
outputs�F���ߍ��݉摜���o�͂���ꏊ
exe_file�F7z.exe�ւ̐�΃p�X(7zip�Ƀp�X���ʂ��Ă�ꍇ��"7z"�����ł��ǂ�)

## �g����

�ȉ��̂悤�ȍ\���ŗ��p�\

�t�H���_��t�@�C���𖄂ߍ���
```
python file2png.py --src "C:\DreamBooth\" "C:\Hypernetwork" "D:\riffusion-model-v1.ckpt"
```

�߂���
```
python png2file.py --src "C:\DreamBooth-S7e4H1ln16-.001.png" "C:\DreamBooth-S7e4H1ln16-.002.png" "C:\DreamBooth-S7e4H1ln16-.003.png"
```

## Asr���[�U�[����

for_Asr_User���ɃX�N���v�g�y�уR�}���h��`�t�@�C��������̂ŁA�R�}���hID���D���ȃz�b�g�L�[�Ɋ���U��
�t�@�C����I��������ԂŃz�b�g�L�[�������Ζ��ߍ��݁E�߂������s�ł���
��file2png.py�Apng2file.py�Apython.exe�����ꂼ���΃p�X�ŏ����Ă邽�ߗv��������

## ���̑�

- ���ߍ��ݐ��png�t�@�C����ǉ����ėǂ��H
  - �ǂ��B5000�����x�͂������������Â炭�Ă���������������Ȃ��B

- ���ߍ��ݐ�̉摜�̍Œ�T�C�Y�͂���H
  - �����B�摜�Ƃ��Ă̕\�����e���ω����Ȃ��B

- 100MB�Ƃ�������������H
  - �����B�f�J������Ɖ�������100MB�ɂ��Ă��邾���B
  - �����⏕�`�����N�Ɏ��߂��2GB�����ł���K�v�͂��邪37�s�ڂ�-v100m��ς��邱�ƂŒ����\�B

- �����k�ł���K�v������H
  - �����B���k�v�Z���Ԃ�Z�����邽�߁B

- �������k�t�@�C�������̂܂ܖ��ߍ��܂��Ĉ��k���Ă闝�R�́H
  - ���������͍Ō�̃t�@�C���ɂ���EOCD���������ߎ��o���Ȃ��Ȃ�
