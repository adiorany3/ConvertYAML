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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS` (url=221ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-98MS` (url=239ms, nekobox=244ms, status=yes)
3. `AKUN-003-GO-DADDY-COM-LLC-VLESS-WS-100MS` (url=234ms, nekobox=301ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-109MS` (url=324ms, nekobox=258ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-105MS` (url=230ms, nekobox=215ms, status=no)
6. `AKUN-006-DEV-VLESS-WS-106MS` (url=218ms, nekobox=211ms, status=no)
7. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS`
9. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS`
10. `AKUN-010-DEV-VLESS-WS-122MS` (url=249ms, nekobox=261ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS`
12. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-130MS` (url=243ms, nekobox=206ms, status=no)
14. `AKUN-010-CLOUDFLARE-VLESS-WS-118MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-138MS` (url=257ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-112MS` (url=228ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-128MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-370MS` (url=756ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-403MS` (url=866ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-376MS` (url=749ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-408MS` (url=912ms, status=HTTP 204)
22. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-439MS` (url=844ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-441MS` (url=852ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-388MS` (url=765ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-731MS` (url=1070ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
