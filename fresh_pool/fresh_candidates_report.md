# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-97MS` (url=225ms, nekobox=244ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-69MS` (url=199ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=218ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=214ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-111MS` (url=217ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=224ms, nekobox=242ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-90MS` (url=203ms, nekobox=237ms, status=yes)
8. `AKUN-008-VULTR-VLESS-WS-104MS` (url=202ms, nekobox=254ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=217ms, nekobox=245ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=224ms, nekobox=246ms, status=yes)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-115MS` (url=220ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-252MS` (url=509ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-260MS` (url=547ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-226MS` (url=494ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-252MS` (url=559ms, status=HTTP 204)
16. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-254MS` (url=560ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-302MS` (url=592ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-283MS` (url=554ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-131MS` (url=216ms, status=HTTP 204)
20. `AKUN-033-UNKNOWN-VLESS-WS-532MS` (url=864ms, status=HTTP 204)
21. `AKUN-034-UNKNOWN-VLESS-WS-391MS` (url=761ms, status=HTTP 204)
22. `AKUN-035-UNKNOWN-VLESS-WS-673MS` (url=934ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
