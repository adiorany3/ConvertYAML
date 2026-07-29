# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-HOSTWINDS-17-7-VLESS-WS-58MS` (url=202ms, nekobox=249ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-62MS` (url=200ms, nekobox=237ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-74MS` (url=199ms, nekobox=230ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-72MS` (url=220ms, nekobox=236ms, status=yes)
5. `AKUN-005-SEECK-VLESS-WS-74MS` (url=214ms, nekobox=221ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-66MS`
7. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS` (url=213ms, nekobox=171ms, status=no)
8. `AKUN-007-HOSTINGER-VLESS-WS-87MS`
9. `AKUN-008-EU-VLESS-WS-74MS`
10. `AKUN-009-EU-VLESS-WS-71MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-67MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-66MS` (url=222ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-64MS` (url=209ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-73MS` (url=226ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-63MS` (url=197ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-68MS` (url=243ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-117MS` (url=337ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-107MS` (url=219ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-159MS` (url=249ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-156MS` (url=224ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-215MS` (url=509ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-225MS` (url=922ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-391MS` (url=655ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-502MS` (url=839ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
