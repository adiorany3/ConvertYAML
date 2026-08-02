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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-85MS` (url=340ms, nekobox=384ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=374ms, nekobox=400ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-95MS` (url=360ms, nekobox=353ms, status=yes)
4. `AKUN-004-CCWU-VLESS-WS-88MS` (url=380ms, nekobox=387ms, status=yes)
5. `AKUN-005-SPEEDTEST-VLESS-WS-86MS` (url=278ms, nekobox=210ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS`
11. `AKUN-011-SPEEDTEST-VLESS-WS-92MS` (url=282ms, nekobox=184ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=285ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=390ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=326ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-121MS` (url=387ms, status=HTTP 204)
17. `AKUN-017-MYBB-VLESS-WS-98MS` (url=356ms, status=HTTP 204)
18. `AKUN-018-MEDIUM-VLESS-WS-112MS` (url=358ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-93MS` (url=351ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-108MS` (url=297ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-109MS` (url=331ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-153MS` (url=415ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-286MS` (url=629ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-336MS` (url=614ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-212MS` (url=511ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
