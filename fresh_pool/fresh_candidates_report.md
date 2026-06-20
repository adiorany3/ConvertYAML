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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-68MS` (url=217ms, nekobox=227ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=229ms, nekobox=182ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS`
4. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-102MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-88MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS`
8. `AKUN-007-U1HOST-FRA-VLESS-WS-120MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-132MS`
12. `AKUN-012-DIGITALOCEAN-VLESS-WS-102MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-NETCUP-VLESS-WS-118MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-128MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-79MS` (url=202ms, status=HTTP 204)
16. `AKUN-016-NET-NL-VLESS-WS-96MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-HOSTOFF-NET-VLESS-WS-95MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-243MS` (url=563ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-252MS` (url=554ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-254MS` (url=555ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-240MS` (url=498ms, status=HTTP 204)
22. `AKUN-022-VULTR-VLESS-WS-81MS` (url=216ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-226MS` (url=489ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-382MS` (url=557ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-230MS` (url=516ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
