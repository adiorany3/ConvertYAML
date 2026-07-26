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
1. `AKUN-001-UNKNOWN-VLESS-WS-71MS` (url=218ms, nekobox=251ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-71MS` (url=227ms, nekobox=245ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-78MS` (url=219ms, nekobox=252ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-69MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS`
6. `AKUN-006-UNKNOWN-VLESS-WS-81MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-104MS` (url=224ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-113MS` (url=224ms, status=HTTP 204)
13. `AKUN-014-EU-VLESS-WS-92MS` (url=206ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-105MS` (url=211ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-100MS` (url=202ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-124MS` (url=206ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-128MS` (url=233ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-195MS` (url=221ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-176MS` (url=374ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-135MS` (url=390ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-133MS` (url=968ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-338MS` (url=706ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-350MS` (url=776ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-375MS` (url=748ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-368MS` (url=753ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
