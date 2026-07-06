# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=219ms, nekobox=252ms, status=yes)
2. `AKUN-002-INTERNETWORKS-45-131-208-VLESS-WS-79MS` (url=231ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=241ms, nekobox=253ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-61MS` (url=216ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=281ms, nekobox=188ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS`
7. `AKUN-007-NODEJS-VLESS-WS-87MS` (url=238ms, nekobox=176ms, status=no)
8. `AKUN-006-CLOUDFLARE-VLESS-WS-104MS`
9. `AKUN-007-WEYRO-NET-VLESS-WS-89MS`
10. `AKUN-008-WPENG-VLESS-WS-64MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-357MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-352MS`
13. `AKUN-017-WPENG-VLESS-WS-400MS` (url=941ms, status=HTTP 204)
14. `AKUN-018-CLOUDFLARE-VLESS-WS-398MS` (url=865ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-366MS` (url=850ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-379MS` (url=811ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-431MS` (url=1071ms, status=HTTP 204)
18. `AKUN-022-CLOUDFLARE-VLESS-WS-366MS` (url=740ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-657MS` (url=1061ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-690MS` (url=1095ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-780MS` (url=1241ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
