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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=220ms, nekobox=239ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-65MS` (url=210ms, nekobox=241ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=230ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=198ms, nekobox=180ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=196ms, nekobox=190ms, status=no)
7. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-64MS`
9. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS`
10. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-83MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-70MS`
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-125MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-100MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-171MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-341MS` (url=727ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-342MS` (url=757ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-365MS` (url=845ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-323MS` (url=643ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-385MS` (url=848ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-403MS` (url=816ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-394MS` (url=849ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-395MS` (url=866ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
