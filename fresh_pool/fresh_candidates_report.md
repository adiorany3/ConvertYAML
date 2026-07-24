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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=199ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=203ms, nekobox=229ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-69MS`
4. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-80MS`
5. `AKUN-005-UNKNOWN-VLESS-WS-82MS`
6. `AKUN-006-LEVIKOGJGFDD-VLESS-WS-77MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-58MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-76MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS` (url=208ms, nekobox=254ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-114MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-82MS` (url=210ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-77MS` (url=222ms, status=HTTP 204)
13. `AKUN-014-ZVC-VLESS-WS-90MS` (url=209ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-82MS` (url=215ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-82MS` (url=229ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-132MS` (url=226ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-116MS` (url=226ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-136MS` (url=196ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-78MS` (url=213ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-143MS` (url=219ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-142MS` (url=232ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-129MS` (url=224ms, status=HTTP 204)
23. `AKUN-024-ZVC-VLESS-WS-156MS` (url=206ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-215MS` (url=502ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-229MS` (url=497ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
