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
1. `AKUN-001-UK-GB-DCL-01-20191003-VLESS-WS-72MS` (url=216ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=229ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=213ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS` (url=213ms, nekobox=240ms, status=yes)
5. `AKUN-005-VULTR-VLESS-WS-85MS` (url=210ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-121MS` (url=202ms, nekobox=237ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-131MS` (url=214ms, nekobox=7176ms, status=no)
8. `AKUN-007-VULTR-VLESS-WS-115MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-124MS` (url=210ms, nekobox=7173ms, status=no)
10. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS`
11. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-220MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-256MS` (url=559ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-274MS` (url=551ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-271MS` (url=582ms, status=HTTP 204)
16. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-91MS` (url=217ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-285MS` (url=513ms, status=HTTP 204)
18. `AKUN-024-UNKNOWN-VLESS-WS-459MS` (url=669ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-270MS` (url=548ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-86MS` (url=218ms, status=HTTP 204)
21. `AKUN-028-BROADNNET-KR-VLESS-WS-99MS` (url=597ms, status=HTTP 204)
22. `AKUN-030-CLOUDFLARE-VLESS-WS-227MS` (url=536ms, status=HTTP 204)
23. `AKUN-032-RS-RAPIDSEEDBOX-20190717-VLESS-WS-483MS` (url=780ms, status=HTTP 204)
24. `AKUN-035-DEV-VLESS-WS-711MS` (url=855ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
