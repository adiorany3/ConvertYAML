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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=211ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS` (url=217ms, nekobox=241ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-65MS` (url=214ms, nekobox=241ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-65MS` (url=216ms, nekobox=236ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-79MS` (url=207ms, nekobox=239ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=200ms, nekobox=243ms, status=yes)
7. `AKUN-007-PAGES-VLESS-WS-74MS` (url=225ms, nekobox=226ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS` (url=212ms, nekobox=7178ms, status=no)
9. `AKUN-009-SPEEDTEST-VLESS-WS-97MS` (url=227ms, nekobox=170ms, status=no)
10. `AKUN-010-SPEEDTEST-VLESS-WS-102MS` (url=228ms, nekobox=170ms, status=no)
11. `AKUN-008-UNKNOWN-VLESS-WS-90MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS`
13. `AKUN-010-LEVIKOGJGFDD-VLESS-WS-113MS`
14. `AKUN-014-UNKNOWN-VLESS-WS-133MS` (url=200ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-74MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-MYBB-VLESS-WS-128MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-106MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-104MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-MEDIUM-VLESS-WS-130MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-340MS` (url=795ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-453MS` (url=1007ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-493MS` (url=857ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-654MS` (url=1088ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-703MS` (url=1136ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-698MS` (url=1123ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
