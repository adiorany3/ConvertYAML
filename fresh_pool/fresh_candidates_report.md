# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 16
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 22

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-090227-VLESS-WS-98MS` (url=219ms, nekobox=274ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS` (url=246ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-112MS` (url=237ms, nekobox=290ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-105MS` (url=246ms, nekobox=251ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-114MS` (url=238ms, nekobox=325ms, status=yes)
6. `AKUN-006-BROADNNET-KR-VLESS-WS-93MS` (url=225ms, nekobox=293ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-140MS` (url=218ms, nekobox=237ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-389MS` (url=783ms, nekobox=822ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-396MS` (url=785ms, nekobox=815ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-382MS` (url=789ms, nekobox=821ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-430MS` (url=862ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-410MS` (url=862ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-416MS` (url=822ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-414MS` (url=837ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-792MS` (url=6858ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-818MS` (url=2417ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
