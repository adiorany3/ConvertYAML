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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-64MS` (url=202ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=237ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=232ms, nekobox=253ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS` (url=217ms, nekobox=350ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=209ms, nekobox=243ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=213ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS` (url=221ms, nekobox=259ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS` (url=235ms, nekobox=229ms, status=yes)
9. `AKUN-009-UK-GB-DCL-01-20191003-VLESS-WS-83MS` (url=234ms, nekobox=182ms, status=no)
10. `AKUN-009-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-111MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-116MS`
12. `AKUN-012-GO-DADDY-COM-LLC-VLESS-WS-100MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-OPENAI-VLESS-WS-81MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-124MS` (url=235ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-356MS` (url=754ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-346MS` (url=755ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-377MS` (url=825ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-395MS` (url=833ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-386MS` (url=840ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-361MS` (url=769ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-384MS` (url=844ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-686MS` (url=1031ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-760MS` (url=1218ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-846MS` (url=1452ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-857MS` (url=1625ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
