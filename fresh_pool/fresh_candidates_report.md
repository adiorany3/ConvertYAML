# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=226ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS` (url=210ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=215ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=216ms, nekobox=263ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-99MS` (url=230ms, nekobox=253ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS` (url=260ms, nekobox=283ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-95MS` (url=236ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-119MS` (url=225ms, nekobox=269ms, status=yes)
9. `AKUN-009-US-VLESS-WS-119MS` (url=245ms, nekobox=260ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=212ms, nekobox=263ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-126MS` (url=218ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-108MS` (url=249ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-119MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-UK-GB-DCL-01-20191003-VLESS-WS-146MS` (url=301ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-138MS` (url=322ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-138MS` (url=288ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-121MS` (url=248ms, status=HTTP 204)
18. `AKUN-018-GO-DADDY-COM-LLC-VLESS-WS-148MS` (url=275ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-172MS` (url=329ms, status=HTTP 204)
20. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-262MS` (url=400ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-384MS` (url=768ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-166MS` (url=371ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-395MS` (url=898ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-405MS` (url=1075ms, status=HTTP 204)
25. `AKUN-026-SPEEDTEST-VLESS-WS-436MS` (url=889ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
