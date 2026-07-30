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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=219ms, nekobox=243ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=217ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=218ms, nekobox=244ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-62MS` (url=202ms, nekobox=250ms, status=yes)
5. `AKUN-005-ZOOM-VLESS-WS-76MS` (url=203ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=199ms, nekobox=238ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-95MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-108MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-72MS` (url=225ms, nekobox=180ms, status=no)
10. `AKUN-011-CLOUDFLARE-VLESS-WS-62MS` (url=225ms, nekobox=175ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-107MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-128MS`
13. `AKUN-015-CLOUDFLARE-VLESS-WS-110MS` (url=229ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-115MS` (url=198ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-157MS` (url=305ms, status=HTTP 204)
16. `AKUN-018-SPEEDTEST-VLESS-WS-79MS` (url=209ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-135MS` (url=257ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-222MS` (url=507ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-241MS` (url=802ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-353MS` (url=475ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-320MS` (url=693ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-415MS` (url=711ms, status=HTTP 204)
23. `AKUN-028-AS210546-IPV4-VLESS-WS-472MS` (url=672ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-389MS` (url=601ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-510MS` (url=840ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
