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
1. `AKUN-001-UNKNOWN-VLESS-WS-92MS` (url=421ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-98MS` (url=235ms, nekobox=234ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-91MS` (url=223ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=211ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-106MS` (url=216ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-114MS` (url=212ms, nekobox=235ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-114MS` (url=241ms, nekobox=292ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-122MS` (url=213ms, nekobox=254ms, status=yes)
9. `AKUN-009-NET-82-21-84-0-24-VLESS-WS-138MS` (url=254ms, nekobox=311ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=233ms, nekobox=273ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-127MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-114MS` (url=274ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-128MS` (url=241ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-129MS` (url=289ms, status=HTTP 204)
15. `AKUN-015-SHOPIFY-VLESS-WS-131MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-146MS` (url=209ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-131MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-145MS` (url=266ms, status=HTTP 204)
19. `AKUN-019-US-VLESS-WS-127MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-117MS` (url=241ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-121MS` (url=210ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-106MS` (url=795ms, status=HTTP 204)
23. `AKUN-023-POSHAKTAT-VLESS-WS-291MS` (url=835ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-364MS` (url=744ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-379MS` (url=790ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
