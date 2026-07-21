# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-105MS` (url=273ms, nekobox=293ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-106MS` (url=226ms, nekobox=252ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-114MS` (url=223ms, nekobox=245ms, status=yes)
4. `AKUN-004-MYBB-VLESS-WS-129MS` (url=228ms, nekobox=287ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-129MS` (url=227ms, nekobox=263ms, status=yes)
6. `AKUN-006-1PASSWORD-VLESS-WS-109MS` (url=221ms, nekobox=282ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-134MS` (url=229ms, nekobox=277ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-136MS` (url=238ms, nekobox=209ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-201MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-275MS`
11. `AKUN-010-CONFLU-VLESS-WS-386MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-376MS` (url=757ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-407MS` (url=826ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-407MS` (url=862ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-654MS` (url=816ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-654MS` (url=409ms, status=HTTP 204)
17. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-690MS` (url=1231ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-718MS` (url=1144ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-693MS` (url=1155ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-738MS` (url=1181ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-746MS` (url=1129ms, status=HTTP 204)
22. `AKUN-031-CLOUDFLARE-VLESS-WS-765MS` (url=745ms, status=HTTP 204)
23. `AKUN-034-CLOUDFLARE-VLESS-WS-592MS` (url=745ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
