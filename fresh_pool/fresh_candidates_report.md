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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=242ms, nekobox=261ms, status=yes)
2. `AKUN-002-WPENG-VLESS-WS-76MS` (url=240ms, nekobox=284ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=233ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=235ms, nekobox=261ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS` (url=258ms, nekobox=273ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS` (url=235ms, nekobox=265ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=225ms, nekobox=281ms, status=yes)
8. `AKUN-008-WEYRO-NET-VLESS-WS-77MS` (url=253ms, nekobox=262ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=239ms, nekobox=264ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-76MS` (url=240ms, nekobox=281ms, status=yes)
11. `AKUN-011-UK-GB-DCL-01-20191003-VLESS-WS-79MS` (url=230ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-100MS` (url=265ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-85MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-76MS` (url=242ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-104MS` (url=241ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-101MS` (url=244ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-88MS` (url=250ms, status=HTTP 204)
18. `AKUN-018-1PASSWORD-VLESS-WS-109MS` (url=240ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-86MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-98MS` (url=275ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-118MS` (url=249ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-266MS` (url=559ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-280MS` (url=627ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-252MS` (url=563ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-281MS` (url=607ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
