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
1. `AKUN-001-UNKNOWN-VLESS-WS-89MS` (url=232ms, nekobox=261ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS` (url=217ms, nekobox=264ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS` (url=228ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=209ms, nekobox=228ms, status=no)
5. `AKUN-005-DEV-VLESS-WS-94MS` (url=223ms, nekobox=227ms, status=no)
6. `AKUN-006-DEV-VLESS-WS-123MS` (url=210ms, nekobox=204ms, status=no)
7. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-102MS`
8. `AKUN-005-CLOUDFLARE-VLESS-WS-116MS`
9. `AKUN-006-BROADNNET-KR-VLESS-WS-147MS`
10. `AKUN-007-CLOUDFLARE-VLESS-WS-145MS`
11. `AKUN-008-BROADNNET-KR-VLESS-WS-182MS`
12. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-175MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-303MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-297MS` (url=625ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-309MS` (url=527ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-282MS` (url=544ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-307MS` (url=610ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-209MS` (url=319ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-365MS` (url=608ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-487MS` (url=1745ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-314MS` (url=528ms, status=HTTP 204)
22. `AKUN-027-RS-RAPIDSEEDBOX-20190717-VLESS-WS-525MS` (url=5704ms, status=HTTP 204)
23. `AKUN-029-GAMETVR-VLESS-WS-531MS` (url=890ms, status=HTTP 204)
24. `AKUN-033-APPLESERAJ-VLESS-WS-773MS` (url=1127ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
