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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=217ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=229ms, nekobox=296ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=234ms, nekobox=292ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS` (url=214ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-62MS` (url=217ms, nekobox=265ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-73MS` (url=249ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=230ms, nekobox=250ms, status=yes)
8. `AKUN-008-NODEHOST-VLESS-WS-88MS` (url=254ms, nekobox=273ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS` (url=234ms, nekobox=260ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-114MS` (url=221ms, nekobox=247ms, status=yes)
11. `AKUN-011-HETZNER-VLESS-WS-110MS` (url=218ms, status=HTTP 204)
12. `AKUN-012-US-VLESS-WS-94MS` (url=241ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-125MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-120MS` (url=271ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-99MS` (url=263ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-77MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-PAGES-VLESS-WS-126MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-HETZNER-VLESS-WS-146MS` (url=248ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-185MS` (url=361ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-373MS` (url=771ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-367MS` (url=3715ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-351MS` (url=793ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-397MS` (url=864ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-379MS` (url=1609ms, status=HTTP 204)
25. `AKUN-029-QZZ-VLESS-WS-563MS` (url=1171ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
