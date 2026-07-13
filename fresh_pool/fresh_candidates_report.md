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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=232ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS` (url=208ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=228ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-101MS` (url=214ms, nekobox=267ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-84MS` (url=203ms, nekobox=232ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=232ms, nekobox=279ms, status=yes)
7. `AKUN-007-PUBLICDOMAINREGISTRY-NET-VLESS-WS-88MS` (url=204ms, nekobox=252ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=204ms, nekobox=238ms, status=no)
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-98MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-105MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-122MS` (url=241ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-100MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-105MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-103MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-134MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-132MS` (url=201ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-160MS` (url=321ms, status=HTTP 204)
20. `AKUN-020-HETZNER-VLESS-WS-170MS` (url=286ms, status=HTTP 204)
21. `AKUN-021-WTO-VLESS-WS-142MS` (url=267ms, status=HTTP 204)
22. `AKUN-022-HETZNER-VLESS-WS-145MS` (url=247ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-256MS` (url=604ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-259MS` (url=590ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-259MS` (url=1562ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
