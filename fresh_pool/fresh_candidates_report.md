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
1. `AKUN-001-ZOOM-VLESS-WS-61MS` (url=226ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=267ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=265ms, nekobox=274ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=262ms, nekobox=308ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=235ms, nekobox=276ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-85MS` (url=240ms, nekobox=262ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=284ms, nekobox=267ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=290ms, nekobox=271ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-80MS` (url=229ms, nekobox=269ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=241ms, nekobox=256ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-77MS` (url=250ms, status=HTTP 204)
12. `AKUN-012-AMAZON-VLESS-WS-148MS` (url=247ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-299MS` (url=568ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-303MS` (url=639ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-310MS` (url=650ms, status=HTTP 204)
16. `AKUN-020-UNKNOWN-VLESS-WS-482MS` (url=861ms, status=HTTP 204)
17. `AKUN-021-UNKNOWN-VLESS-WS-243MS` (url=657ms, status=HTTP 204)
18. `AKUN-022-UNKNOWN-VLESS-WS-285MS` (url=399ms, status=HTTP 204)
19. `AKUN-024-UNKNOWN-VLESS-WS-596MS` (url=1005ms, status=HTTP 204)
20. `AKUN-026-HIKVISIONPLUS-VLESS-WS-608MS` (url=814ms, status=HTTP 204)
21. `AKUN-028-UNKNOWN-VLESS-WS-883MS` (url=662ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
