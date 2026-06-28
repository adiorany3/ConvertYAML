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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=229ms, nekobox=248ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-70MS` (url=221ms, nekobox=269ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-82MS` (url=249ms, nekobox=249ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-81MS` (url=218ms, nekobox=256ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-74MS` (url=386ms, nekobox=238ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=222ms, nekobox=260ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-86MS` (url=209ms, nekobox=265ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=217ms, nekobox=258ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=256ms, nekobox=273ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-101MS` (url=228ms, nekobox=263ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-80MS` (url=225ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-359MS` (url=708ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-365MS` (url=600ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-395MS` (url=827ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-377MS` (url=837ms, status=HTTP 204)
17. `AKUN-018-CONFLU-VLESS-WS-364MS` (url=764ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-352MS` (url=777ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-409MS` (url=865ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-414MS` (url=859ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-405MS` (url=857ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-729MS` (url=1174ms, status=HTTP 204)
23. `AKUN-031-CLOUDFLARE-VLESS-WS-794MS` (url=1305ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-875MS` (url=1244ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
