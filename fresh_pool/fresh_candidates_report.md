# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-GOV-VLESS-WS-71MS` (url=228ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=242ms, nekobox=271ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=245ms, nekobox=304ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS` (url=231ms, nekobox=292ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=232ms, nekobox=255ms, status=yes)
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-109MS` (url=241ms, nekobox=263ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=234ms, nekobox=296ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-73MS` (url=246ms, nekobox=261ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-101MS` (url=268ms, nekobox=264ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-116MS` (url=260ms, nekobox=283ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-111MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS` (url=262ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-93MS` (url=301ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-310MS` (url=631ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-323MS` (url=655ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-322MS` (url=610ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-299MS` (url=626ms, status=HTTP 204)
18. `AKUN-019-CONFLU-VLESS-WS-297MS` (url=587ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-256MS` (url=566ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-291MS` (url=600ms, status=HTTP 204)
21. `AKUN-032-CLOUDFLARE-VLESS-WS-576MS` (url=954ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
