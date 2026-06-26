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
1. `AKUN-001-ORACLE-VLESS-WS-86MS` (url=205ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-102MS` (url=209ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=210ms, nekobox=258ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-107MS` (url=239ms, nekobox=254ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS` (url=231ms, nekobox=261ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-112MS` (url=253ms, nekobox=282ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-91MS` (url=204ms, nekobox=259ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-145MS` (url=238ms, nekobox=268ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS` (url=231ms, nekobox=271ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-139MS` (url=216ms, nekobox=263ms, status=yes)
11. `AKUN-011-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-113MS` (url=213ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-129MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-147MS` (url=276ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-94MS` (url=269ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-112MS` (url=258ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-245MS` (url=512ms, status=HTTP 204)
18. `AKUN-018-OCTOPUSSS5-VLESS-WS-264MS` (url=582ms, status=HTTP 204)
19. `AKUN-019-MICROSOFT-VLESS-WS-270MS` (url=578ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-266MS` (url=520ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-282MS` (url=554ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-294MS` (url=606ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-308MS` (url=524ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-273MS` (url=572ms, status=HTTP 204)
25. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-485MS` (url=821ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
