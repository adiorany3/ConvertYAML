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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=216ms, nekobox=186ms, status=no)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=225ms, nekobox=185ms, status=no)
3. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS`
4. `AKUN-004-DEV-VLESS-WS-73MS` (url=222ms, nekobox=182ms, status=no)
5. `AKUN-002-UNKNOWN-VLESS-WS-73MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-66MS` (url=216ms, nekobox=196ms, status=no)
7. `AKUN-007-DEV-VLESS-WS-67MS` (url=226ms, nekobox=178ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=224ms, nekobox=175ms, status=no)
9. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS`
10. `AKUN-004-NET-14-102-228-0-23-VLESS-WS-101MS`
11. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS`
12. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS`
13. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS`
14. `AKUN-008-CLOUDFLARE-VLESS-WS-109MS`
15. `AKUN-009-CLOUDFLARE-VLESS-WS-125MS`
16. `AKUN-010-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-105MS`
17. `AKUN-017-CLOUDFLARE-VLESS-WS-224MS` (url=500ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-252MS` (url=537ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-255MS` (url=480ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-254MS` (url=622ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-246MS` (url=550ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-242MS` (url=497ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-468MS` (url=550ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-271MS` (url=545ms, status=HTTP 204)
25. `AKUN-033-UNKNOWN-VLESS-WS-527MS` (url=867ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
