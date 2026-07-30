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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=214ms, nekobox=227ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=214ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=219ms, nekobox=258ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=215ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS` (url=207ms, nekobox=240ms, status=yes)
6. `AKUN-006-ADF-VLESS-WS-86MS` (url=216ms, nekobox=236ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS` (url=209ms, nekobox=235ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=213ms, nekobox=245ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-83MS` (url=216ms, nekobox=247ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS` (url=195ms, nekobox=228ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-110MS` (url=206ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-76MS` (url=196ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-102MS` (url=203ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-102MS` (url=213ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-75MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-89MS` (url=198ms, status=HTTP 204)
19. `AKUN-019-008500-VLESS-WS-101MS` (url=197ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-77MS` (url=204ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-99MS` (url=216ms, status=HTTP 204)
22. `AKUN-022-ALIBABA-VLESS-WS-82MS` (url=208ms, status=HTTP 204)
23. `AKUN-023-DEV-VLESS-WS-127MS` (url=229ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-128MS` (url=315ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-84MS` (url=222ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
