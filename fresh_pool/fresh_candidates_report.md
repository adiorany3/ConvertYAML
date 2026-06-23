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
1. `AKUN-001-9889888-VLESS-WS-85MS` (url=231ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=236ms, nekobox=230ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=221ms, nekobox=243ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS` (url=256ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-109MS` (url=230ms, nekobox=228ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-115MS` (url=219ms, nekobox=280ms, status=yes)
7. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-95MS` (url=207ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=211ms, nekobox=232ms, status=no)
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-140MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS`
11. `AKUN-010-BROADNNET-KR-VLESS-WS-123MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-258MS` (url=522ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-254MS` (url=600ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-263MS` (url=608ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-105MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-275MS` (url=609ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-289MS` (url=580ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-147MS` (url=253ms, status=HTTP 204)
19. `AKUN-026-UNKNOWN-VLESS-WS-267MS` (url=565ms, status=HTTP 204)
20. `AKUN-028-VIDBOXCO-VLESS-WS-517MS` (url=728ms, status=HTTP 204)
21. `AKUN-030-CLOUDFLARE-VLESS-WS-262MS` (url=515ms, status=HTTP 204)
22. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-609MS` (url=1682ms, status=HTTP 204)
23. `AKUN-033-UNKNOWN-VLESS-WS-480MS` (url=1798ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-706MS` (url=4164ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
