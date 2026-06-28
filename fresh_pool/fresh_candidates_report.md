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
1. `AKUN-001-9889888-VLESS-WS-64MS` (url=200ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=210ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=213ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=217ms, nekobox=256ms, status=yes)
5. `AKUN-005-ZOOM-VLESS-WS-93MS` (url=206ms, nekobox=239ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=215ms, nekobox=234ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-92MS` (url=220ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=228ms, nekobox=259ms, status=yes)
9. `AKUN-009-BIGCOMMERCE-VLESS-WS-87MS` (url=210ms, nekobox=245ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS` (url=201ms, nekobox=234ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-108MS` (url=214ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-95MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-97MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-80MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-90MS` (url=205ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-134MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-153MS` (url=242ms, status=HTTP 204)
18. `AKUN-018-CONFLU-VLESS-WS-228MS` (url=479ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-258MS` (url=540ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-247MS` (url=573ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-248MS` (url=502ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-268MS` (url=544ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-270MS` (url=545ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-275MS` (url=603ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-230MS` (url=486ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
