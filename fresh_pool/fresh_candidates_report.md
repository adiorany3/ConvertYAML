# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-84MS` (url=222ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-102MS` (url=220ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS` (url=200ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-95MS` (url=222ms, nekobox=233ms, status=yes)
5. `AKUN-005-VULTR-VLESS-WS-100MS` (url=229ms, nekobox=263ms, status=yes)
6. `AKUN-006-ALIBABA-VLESS-WS-83MS` (url=225ms, nekobox=229ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=202ms, nekobox=236ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS` (url=222ms, nekobox=256ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS` (url=203ms, nekobox=232ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=248ms, nekobox=348ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-249MS` (url=516ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-259MS` (url=497ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-274MS` (url=517ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-268MS` (url=572ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-279MS` (url=569ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-274MS` (url=557ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-273MS` (url=606ms, status=HTTP 204)
18. `AKUN-031-UNKNOWN-VLESS-WS-524MS` (url=876ms, status=HTTP 204)
19. `AKUN-033-UNKNOWN-VLESS-WS-583MS` (url=995ms, status=HTTP 204)
20. `AKUN-035-UNKNOWN-VLESS-WS-595MS` (url=2065ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
