# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-72MS` (url=238ms, nekobox=260ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=241ms, nekobox=273ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=244ms, nekobox=263ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS` (url=272ms, nekobox=270ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-120MS` (url=292ms, nekobox=279ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=246ms, nekobox=276ms, status=yes)
7. `AKUN-007-ALIBABA-VLESS-WS-112MS` (url=250ms, nekobox=271ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS` (url=301ms, nekobox=297ms, status=yes)
9. `AKUN-009-BROADNNET-KR-VLESS-WS-142MS` (url=250ms, nekobox=314ms, status=yes)
10. `AKUN-010-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-99MS` (url=244ms, nekobox=271ms, status=yes)
11. `AKUN-011-BROADNNET-KR-VLESS-WS-96MS` (url=282ms, status=HTTP 204)
12. `AKUN-012-DIGITALOCEAN-VLESS-WS-106MS` (url=268ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-261MS` (url=564ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-294MS` (url=633ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-289MS` (url=620ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-273MS` (url=560ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-302MS` (url=656ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-312MS` (url=663ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-296MS` (url=571ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-530MS` (url=782ms, status=HTTP 204)
21. `AKUN-032-UNKNOWN-VLESS-WS-587MS` (url=961ms, status=HTTP 204)
22. `AKUN-035-RS-RAPIDSEEDBOX-20190717-VLESS-WS-652MS` (url=1656ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
