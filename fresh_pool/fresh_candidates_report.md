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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=226ms, nekobox=251ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-82MS` (url=225ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=242ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=224ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=271ms, nekobox=254ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-94MS` (url=207ms, nekobox=249ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=226ms, nekobox=231ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-91MS` (url=205ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=217ms, nekobox=263ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-105MS` (url=213ms, nekobox=246ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-104MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-107MS` (url=286ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-118MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-122MS` (url=247ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-124MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-146MS` (url=261ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-266MS` (url=526ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-292MS` (url=649ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-291MS` (url=531ms, status=HTTP 204)
20. `AKUN-022-WPENG-VLESS-WS-302MS` (url=627ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-273MS` (url=547ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-311MS` (url=654ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-303MS` (url=429ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-420MS` (url=771ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-535MS` (url=927ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
