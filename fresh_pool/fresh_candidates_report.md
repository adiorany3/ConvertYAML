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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-87MS` (url=231ms, nekobox=242ms, status=yes)
2. `AKUN-002-COMPREND-NET-VLESS-WS-89MS` (url=234ms, nekobox=289ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-96MS` (url=231ms, nekobox=228ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-105MS` (url=228ms, nekobox=261ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS` (url=425ms, nekobox=236ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS` (url=216ms, nekobox=468ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-119MS` (url=222ms, nekobox=259ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-122MS` (url=212ms, nekobox=255ms, status=yes)
9. `AKUN-009-UK-GB-DCL-01-20191003-VLESS-WS-123MS` (url=222ms, nekobox=255ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-101MS` (url=250ms, nekobox=238ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-95MS` (url=242ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-126MS` (url=273ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-141MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-105MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-138MS` (url=237ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-348MS` (url=799ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-355MS` (url=754ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-414MS` (url=879ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-393MS` (url=880ms, status=HTTP 204)
21. `AKUN-022-WPENG-VLESS-WS-418MS` (url=847ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-421MS` (url=937ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-364MS` (url=767ms, status=HTTP 204)
24. `AKUN-028-BIGCOMMERCE-VLESS-WS-717MS` (url=1145ms, status=HTTP 204)
25. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-802MS` (url=1350ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
