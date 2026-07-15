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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=249ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=235ms, nekobox=273ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=240ms, nekobox=264ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=245ms, nekobox=256ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=244ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS` (url=258ms, nekobox=279ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-82MS` (url=227ms, nekobox=265ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=261ms, nekobox=263ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=283ms, nekobox=278ms, status=yes)
10. `AKUN-010-DIXONS-VLESS-WS-92MS` (url=246ms, nekobox=294ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-84MS` (url=280ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-131MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-101MS` (url=262ms, status=HTTP 204)
14. `AKUN-014-PUBLICDOMAINREGISTRY-NET-VLESS-WS-134MS` (url=294ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-82MS` (url=256ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-108MS` (url=279ms, status=HTTP 204)
17. `AKUN-017-POLICE-VLESS-WS-118MS` (url=301ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-166MS` (url=310ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-120MS` (url=250ms, status=HTTP 204)
20. `AKUN-020-POLICE-VLESS-WS-136MS` (url=266ms, status=HTTP 204)
21. `AKUN-022-466688-VLESS-WS-79MS` (url=247ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-278MS` (url=638ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-300MS` (url=617ms, status=HTTP 204)
24. `AKUN-028-RS-RAPIDSEEDBOX-20190717-VLESS-WS-301MS` (url=677ms, status=HTTP 204)
25. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-308MS` (url=3089ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
