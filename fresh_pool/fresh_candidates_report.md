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
1. `AKUN-001-UNKNOWN-VLESS-WS-94MS` (url=211ms, nekobox=251ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-87MS` (url=227ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-99MS` (url=204ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=218ms, nekobox=181ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-109MS` (url=229ms, nekobox=192ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-113MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-200MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS`
9. `AKUN-007-WPENG-VLESS-WS-267MS`
10. `AKUN-008-QZZ-VLESS-WS-349MS`
11. `AKUN-009-QZZ-VLESS-WS-339MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-277MS`
13. `AKUN-015-QZZ-VLESS-WS-375MS` (url=646ms, status=HTTP 204)
14. `AKUN-016-QZZ-VLESS-WS-332MS` (url=647ms, status=HTTP 204)
15. `AKUN-017-QZZ-VLESS-WS-339MS` (url=635ms, status=HTTP 204)
16. `AKUN-018-QZZ-VLESS-WS-361MS` (url=629ms, status=HTTP 204)
17. `AKUN-020-QZZ-VLESS-WS-348MS` (url=604ms, status=HTTP 204)
18. `AKUN-021-QZZ-VLESS-WS-424MS` (url=1914ms, status=HTTP 204)
19. `AKUN-022-QZZ-VLESS-WS-341MS` (url=627ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-216MS` (url=520ms, status=HTTP 204)
21. `AKUN-029-BIGCOMMERCE-VLESS-WS-438MS` (url=698ms, status=HTTP 204)
22. `AKUN-032-QZZ-VLESS-WS-375MS` (url=659ms, status=HTTP 204)
23. `AKUN-034-CLOUDFLARE-VLESS-WS-485MS` (url=770ms, status=HTTP 204)
24. `AKUN-035-CLOUDFLARE-VLESS-WS-896MS` (url=2974ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
