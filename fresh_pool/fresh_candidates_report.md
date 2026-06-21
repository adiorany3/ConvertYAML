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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=198ms, nekobox=183ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=227ms, nekobox=193ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS`
7. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS`
8. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-71MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS` (url=196ms, nekobox=187ms, status=no)
10. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=202ms, nekobox=195ms, status=no)
12. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS`
13. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-139MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-225MS`
15. `AKUN-015-CONFLU-VLESS-WS-227MS` (url=523ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-251MS` (url=553ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-259MS` (url=546ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-268MS` (url=568ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-272MS` (url=543ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-238MS` (url=495ms, status=HTTP 204)
21. `AKUN-030-BIGCOMMERCE-VLESS-WS-448MS` (url=704ms, status=HTTP 204)
22. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-479MS` (url=692ms, status=HTTP 204)
23. `AKUN-033-CLOUDFLARE-VLESS-WS-515MS` (url=791ms, status=HTTP 204)
24. `AKUN-035-CLOUDFLARE-VLESS-WS-536MS` (url=883ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
